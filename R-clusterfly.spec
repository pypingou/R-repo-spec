%global packname  clusterfly
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.3
Release:          1%{?dist}
Summary:          Explore clustering interactively using R and GGobi

Group:            Applications/Engineering 
License:          MIT
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-ggplot2 R-reshape R-rggobi 

BuildRequires:    R-devel tex(latex) R-ggplot2 R-reshape R-rggobi 

%description
Visualise clustering algorithms with GGobi.  Contains both general code
for visualising clustering results and specific visualisations for
model-based, hierarchical and SOM clustering.

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
* Fri Dec 02 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.3-1
- initial package for Fedora