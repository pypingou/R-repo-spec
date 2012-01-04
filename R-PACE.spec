%global packname  PACE
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.1.0
Release:          1%{?dist}
Summary:          PACE package

Group:            Applications/Engineering 
License:          GPL
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.1-0.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-akima R-MASS 

BuildRequires:    R-devel tex(latex) R-akima R-MASS 

%description
The core program of this package is Functional Principal Component
Analysis (FPCA), a key technique for functional data analysis, for
sparsely or densely sampled random trajectories and time courses, via the
Principal Analysis by Conditional Estimation (PACE) algorithm.

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
%doc %{rlibdir}/PACE/html
%doc %{rlibdir}/PACE/DESCRIPTION
%{rlibdir}/PACE/INDEX
%{rlibdir}/PACE/R
%{rlibdir}/PACE/help
%{rlibdir}/PACE/NAMESPACE
%{rlibdir}/PACE/Meta
%{rlibdir}/PACE/data

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.1.0-1
- initial package for Fedora