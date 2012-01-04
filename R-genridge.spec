%global packname  genridge
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.5.0
Release:          1%{?dist}
Summary:          Generalized ridge trace plots for ridge regression

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.5-0.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
The genridge package introduces generalizations of the standard univariate
ridge trace plot used in ridge regression and related methods.  These
graphical methods show both bias and precision, by plotting the covariance
ellipsoids of the estimated coefficients, rather than just the estimates

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
%doc %{rlibdir}/genridge/NEWS
%doc %{rlibdir}/genridge/html
%doc %{rlibdir}/genridge/DESCRIPTION
%{rlibdir}/genridge/INDEX
%{rlibdir}/genridge/Meta
%{rlibdir}/genridge/R
%{rlibdir}/genridge/NAMESPACE
%{rlibdir}/genridge/help

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.5.0-1
- initial package for Fedora