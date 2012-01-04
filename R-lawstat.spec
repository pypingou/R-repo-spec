%global packname  lawstat
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          2.3
Release:          1%{?dist}
Summary:          An R package for biostatistics, public policy, and law

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-grDevices R-stats R-mvtnorm R-VGAM 

BuildRequires:    R-devel tex(latex) R-grDevices R-stats R-mvtnorm R-VGAM 

%description
An R software package on statistical tests widely utilized in
biostatistics, public policy and law. Along with the well known tests for
equality of means and variances, randomness, measures of relative
variability etc, the package contains new robust tests of symmetry,
omnibus and directional tests of normality, and their graphical
counterparts such as Robust QQ plot; a robust trend tests for variances
etc. All implemented tests and methods are illustrated by simulations and
real-life examples from legal statistics, economics, and biostatistics.

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
%doc %{rlibdir}/lawstat/html
%doc %{rlibdir}/lawstat/DESCRIPTION
%{rlibdir}/lawstat/R
%{rlibdir}/lawstat/data
%{rlibdir}/lawstat/help
%{rlibdir}/lawstat/INDEX
%{rlibdir}/lawstat/Meta

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2.3-1
- initial package for Fedora