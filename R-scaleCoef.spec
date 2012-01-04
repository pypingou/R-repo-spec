%global packname  scaleCoef
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.0.0
Release:          1%{?dist}
Summary:          Scale regression coefficients

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.0-0.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-car 

BuildRequires:    R-devel tex(latex) R-car 

%description
Scale regression coefficients from model fit object(s) by a user specified
function of the predictor variables of interest or a constant to produce
an object of S3 class scaleCoef. Generic functions are available for
printing, plotting, or ranking scaled regression coefficients by absolute

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
%doc %{rlibdir}/scaleCoef/DESCRIPTION
%doc %{rlibdir}/scaleCoef/html
%{rlibdir}/scaleCoef/help
%{rlibdir}/scaleCoef/R
%{rlibdir}/scaleCoef/INDEX
%{rlibdir}/scaleCoef/Meta

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.0-1
- initial package for Fedora