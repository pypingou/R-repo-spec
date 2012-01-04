%global packname  gbev
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.1.1
Release:          1%{?dist}
Summary:          Gradient Boosted Regression Trees with Errors-in-Variables

Group:            Applications/Engineering 
License:          GPL (version 2 or newer)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-mvtnorm 

BuildRequires:    R-devel tex(latex) R-mvtnorm 

%description
This package performs non-parametric regression when covariates are
measured with error. The models are estimated using gradient boosted
regression trees. Regression is performed using squared error loss, while
binary response regression can be performed using negative log-likelihood

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
%doc %{rlibdir}/gbev/html
%doc %{rlibdir}/gbev/DESCRIPTION
%{rlibdir}/gbev/demo
%{rlibdir}/gbev/R
%{rlibdir}/gbev/libs
%{rlibdir}/gbev/NAMESPACE
%{rlibdir}/gbev/help
%{rlibdir}/gbev/Meta
%{rlibdir}/gbev/INDEX

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.1.1-1
- initial package for Fedora