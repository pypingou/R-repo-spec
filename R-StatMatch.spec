%global packname  StatMatch
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.0.3
Release:          1%{?dist}
Summary:          Statistical Matching

Group:            Applications/Engineering 
License:          EUPL
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-proxy R-lpSolve R-survey 

BuildRequires:    R-devel tex(latex) R-proxy R-lpSolve R-survey 

%description
The package StatMatch provides some R functions to perform statistical
matching, i.e. the integration of two data sources referred to the same
target population which share a number of common variables. Some functions
can also be used to impute missing values in data sets through hot deck
imputation methods. Methods to perform statistical matching when dealing
with data from complex sample surveys are available too.

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
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.3-1
- initial package for Fedora