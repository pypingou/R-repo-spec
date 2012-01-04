%global packname  nga
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.3
Release:          1%{?dist}
Summary:          NGA Earthquake Ground Motion Prediction Equations

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
This package implements the earthquake ground motion prediction equations
developed as part of the Next Generation Attenuation of Ground Motions
(NGA) project coordinated by the Pacific Earthquake Engineering Research
Center (PEER) in 2008. The models implemented in this package are AS08
(Abrahamson & Silva, 2008), BA08 (Boore & Atkinson, 2008), CB08 (Campbell
& Bozorgnia, 2008), and CY08 (Chiou & Youngs, 2008).  This numerical
implementation has been validated by comparing the results for 128,000
test cases against the results obtained using the Fortran implementation
composed by David M. Boore and Kenneth W. Campbell. Users are encouraged
to view U.S. Geological Survey Open-File Report 1296, entitled
"Implementation of the Next Generation Attenuation (NGA) Ground-Motion
Prediction Equations in Fortran and R," by J. Kaklamanos, D. M. Boore, E.
M. Thompson, and K. W. Campbell (2010) for further details on these
programs.  More details (including a change log) are available at

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
%doc %{rlibdir}/nga/DESCRIPTION
%doc %{rlibdir}/nga/html
%{rlibdir}/nga/data
%{rlibdir}/nga/NAMESPACE
%{rlibdir}/nga/INDEX
%{rlibdir}/nga/Meta
%{rlibdir}/nga/help
%{rlibdir}/nga/R

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.3-1
- initial package for Fedora