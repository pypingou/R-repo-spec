%global packname  dgof
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.0
Release:          1%{?dist}
Summary:          Discrete Goodness-of-Fit Tests

Group:            Applications/Engineering 
License:          GPL (>= 2.0)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
This package contains a proposed revision to the stats::ks.test() function
and the associated ks.test.Rd help page.  With one minor exception, it
does not change the existing behavior of ks.test(), and it adds features
necessary for doing one-sample tests with hypothesized discrete
distributions.  The package also contains cvm.test(), for doing one-sample
Cramer-von Mises goodness-of-fit tests.

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
%doc %{rlibdir}/dgof/CITATION
%doc %{rlibdir}/dgof/html
%doc %{rlibdir}/dgof/DESCRIPTION
%{rlibdir}/dgof/Meta
%{rlibdir}/dgof/INDEX
%{rlibdir}/dgof/R
%{rlibdir}/dgof/NAMESPACE
%{rlibdir}/dgof/help

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0-1
- initial package for Fedora