%global packname  chemCal
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.1.27
Release:          1%{?dist}
Summary:          Calibration functions for analytical chemistry

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.1-27.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
chemCal provides simple functions for plotting linear calibration
functions and estimating standard errors for measurements according to the
Handbook of Chemometrics and Qualimetrics: Part A by Massart et al. There
are also functions estimating the limit of detection (LOQ) and limit of
quantification (LOD). The functions work on model objects from -
optionally weighted - linear regression (lm) or robust linear regression
(rlm from the MASS package).

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
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.1.27-1
- initial package for Fedora