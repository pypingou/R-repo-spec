%global packname  scout
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.0.3
Release:          1%{?dist}
Summary:          Implements the Scout method for Covariance-Regularized Regression

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-glasso R-lars 

BuildRequires:    R-devel tex(latex) R-glasso R-lars 

%description
Implements the Scout method for regression, described in
"Covariance-regularized regression and classification for high-dimensional
problems", by Witten and Tibshirani (2008), Journal of the Royal
Statistical Society, Series B 71(3): 615-636.

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
%doc %{rlibdir}/scout/html
%doc %{rlibdir}/scout/DESCRIPTION
%{rlibdir}/scout/R
%{rlibdir}/scout/libs
%{rlibdir}/scout/NAMESPACE
%{rlibdir}/scout/INDEX
%{rlibdir}/scout/help
%{rlibdir}/scout/Meta

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.3-1
- initial package for Fedora