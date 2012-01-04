%global packname  robCompositions
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.5.0
Release:          1%{?dist}
Summary:          Robust Estimation for Compositional Data.

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-utils R-robustbase R-rrcov R-car R-MASS 

BuildRequires:    R-devel tex(latex) R-utils R-robustbase R-rrcov R-car R-MASS 

%description
The package includes methods for imputation of compositional data
including robust methods, (robust) outlier detection for compositional
data, (robust) principal component analysis for compositional data,
(robust) factor analysis for compositional data, (robust) discriminant
analysis for compositional data (Fisher rule) and (robust)
Anderson-Darling normality tests for compositional data as well as popular
log-ratio transformations (alr, clr, ilr, and their inverse

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
%changelog
* Fri Dec 02 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.5.0-1
- initial package for Fedora