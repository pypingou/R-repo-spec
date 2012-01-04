%global packname  ncf
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.1.3
Release:          1%{?dist}
Summary:          spatial nonparametric covariance functions

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.1-3.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
R functions for analyzing spatial (cross-)covariance: the nonparametric
(cross-)covariance, the spline correlogram, the nonparametric phase
coherence function, and related.

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
%doc %{rlibdir}/ncf/DESCRIPTION
%doc %{rlibdir}/ncf/html
%{rlibdir}/ncf/data
%{rlibdir}/ncf/INDEX
%{rlibdir}/ncf/help
%{rlibdir}/ncf/Meta
%{rlibdir}/ncf/NAMESPACE
%{rlibdir}/ncf/R

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.1.3-1
- initial package for Fedora