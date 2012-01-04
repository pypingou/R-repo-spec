%global packname  nlrwr
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.1.0
Release:          1%{?dist}
Summary:          Nonlinear regression with R

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.1-0.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-alr3 R-car R-drc R-HydroMe R-lattice R-lmtest R-MASS R-NISTnls R-nlme R-nls2 R-nlstools R-NRAIA R-sandwich 


BuildRequires:    R-devel tex(latex) R-alr3 R-car R-drc R-HydroMe R-lattice R-lmtest R-MASS R-NISTnls R-nlme R-nls2 R-nlstools R-NRAIA R-sandwich



%description
Datasets and functions for nonlinear regression. Support software for the
book "Nonlinear regression with R".

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
* Sat Dec 10 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.1.0-1
- initial package for Fedora