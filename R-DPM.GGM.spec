%global packname  DPM.GGM
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.14
Release:          1%{?dist}
Summary:          Dirichlet Process Mixtures (DPM) and related models using Gaussian Graphical Models (GGM) for Sparse covariance estimation in heterogeneous samples

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-lattice 

BuildRequires:    R-devel tex(latex) R-lattice 

%description
This package provides functions to estimate sparse covariance in
heterogenous samples using Dirichlet Process Mixtures (DPMs) with Gaussian
Graphical Model (GGM) kernel distributions.

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
%doc %{rlibdir}/DPM.GGM/DESCRIPTION
%doc %{rlibdir}/DPM.GGM/html
%{rlibdir}/DPM.GGM/libs
%{rlibdir}/DPM.GGM/help
%{rlibdir}/DPM.GGM/data
%{rlibdir}/DPM.GGM/NAMESPACE
%{rlibdir}/DPM.GGM/Meta
%{rlibdir}/DPM.GGM/INDEX
%{rlibdir}/DPM.GGM/R

%changelog
* Mon Dec 05 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.14-1
- initial package for Fedora