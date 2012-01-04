%global packname  NRAIA
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.9.8
Release:          1%{?dist}
Summary:          Data sets from "Nonlinear Regression Analysis and Its Applications"

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.9-8.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-lattice R-stats 

BuildRequires:    R-devel tex(latex) R-lattice R-stats 

%description
Datasets from Bates and Watts (1988) "Nonlinear Regression Analysis and
Its Applications" with sample code.

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
%doc %{rlibdir}/NRAIA/DESCRIPTION
%doc %{rlibdir}/NRAIA/html
%{rlibdir}/NRAIA/help
%{rlibdir}/NRAIA/INDEX
%{rlibdir}/NRAIA/Meta
%{rlibdir}/NRAIA/NAMESPACE
%{rlibdir}/NRAIA/R
%{rlibdir}/NRAIA/data

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.9.8-1
- initial package for Fedora