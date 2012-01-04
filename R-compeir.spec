%global packname  compeir
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.0
Release:          1%{?dist}
Summary:          Event-specific incidence rates for competing risks data

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-grid R-lattice R-etm 

BuildRequires:    R-devel tex(latex) R-grid R-lattice R-etm 

%description
The package enables to compute event-specific incidence rates for
competing risks data, to compute rate ratios, event-specific incidence
proportions and cumulative incidence functions from these, and to plot
these in a comprehensive multi-state type graphic.

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
%doc %{rlibdir}/compeir/html
%doc %{rlibdir}/compeir/DESCRIPTION
%{rlibdir}/compeir/data
%{rlibdir}/compeir/Meta
%{rlibdir}/compeir/R
%{rlibdir}/compeir/help
%{rlibdir}/compeir/INDEX
%{rlibdir}/compeir/NAMESPACE

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0-1
- initial package for Fedora