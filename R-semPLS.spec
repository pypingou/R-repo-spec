%global packname  semPLS
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.0.3
Release:          1%{?dist}
Summary:          Structural Equation Modeling Using Partial Least Squares

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.0-3.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-lattice 

BuildRequires:    R-devel tex(latex) R-lattice 

%description
Fits structural equation models using partial least squares (PLS). The PLS
approach is referred to as 'soft-modeling' technique requiring no
distributional assumptions on the observed data.

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
%doc %{rlibdir}/semPLS/DESCRIPTION
%doc %{rlibdir}/semPLS/html
%doc %{rlibdir}/semPLS/NEWS
%{rlibdir}/semPLS/INDEX
%{rlibdir}/semPLS/data
%{rlibdir}/semPLS/R
%{rlibdir}/semPLS/ECSImeasuremod.csv
%{rlibdir}/semPLS/NAMESPACE
%{rlibdir}/semPLS/ECSIstrucmod.csv
%{rlibdir}/semPLS/Meta
%{rlibdir}/semPLS/SmartPLS
%{rlibdir}/semPLS/help

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.3-1
- initial package for Fedora