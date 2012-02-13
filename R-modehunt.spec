%global packname  modehunt
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.0.6
Release:          1%{dist}
Summary:          Multiscale Analysis for Density Functions

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
Given independent and identically distributed observations X(1), ..., X(n)
from a density f, this package provides five methods to perform a
multiscale analysis about f as well as the necessary critical values. The
first method, introduced in Duembgen and Walther (2008), provides
simultaneous confidence statements for the existence and location of local
increases (or decreases) of f, based on all intervals I(all) spanned by
any two observations X(j), X(k). The second method approximates the latter
approach by using only a subset of I(all) and is therefore computationally
much more efficient, but asymptotically equivalent. Omitting the additive
correction term Gamma in either method offers another two approaches which
are more powerful on small scales and less powerful on large scales,
however, not asymptotically minimax optimal anymore. Finally, the block
procedure is a compromise between adding Gamma or not, having intermediate
power properties. The latter is again asymptotically equivalent to the
first and was introduced in Rufibach and Walther (2010).

%prep
%setup -q -c -n %{packname}

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root, -)
%doc %{rlibdir}/modehunt/DESCRIPTION
%doc %{rlibdir}/modehunt/html
%doc %{rlibdir}/modehunt/NEWS
%{rlibdir}/modehunt/data
%{rlibdir}/modehunt/Meta
%{rlibdir}/modehunt/R
%{rlibdir}/modehunt/NAMESPACE
%{rlibdir}/modehunt/help
%{rlibdir}/modehunt/INDEX

%changelog
* Sun Feb 12 2012 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.6-1
- Update to version 1.0.6

* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.5-1
- initial package for Fedora