%global packname  ROI.plugin.symphony
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.0.1
Release:          1%{?dist}
Summary:          ROI-plugin symphony

Group:            Applications/Engineering 
License:          GPL-3
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.0-1.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core


Requires:         R-methods R-ROI R-Rsymphony 

BuildRequires:    R-devel tex(latex) 
BuildRequires:    R-methods R-ROI R-Rsymphony 


%description
This package enhances the R Optimization Infrastructure (ROI) package with
the symphony solver from the COIN-OR suite for solving mixed integer
linear programming (MILP) problems as well as all variants/combinations of
LP, IP.

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
%doc %{rlibdir}/ROI.plugin.symphony/html
%doc %{rlibdir}/ROI.plugin.symphony/DESCRIPTION
%{rlibdir}/ROI.plugin.symphony/Meta
%{rlibdir}/ROI.plugin.symphony/R
%{rlibdir}/ROI.plugin.symphony/NAMESPACE
%{rlibdir}/ROI.plugin.symphony/help

%changelog
* Fri Dec 09 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.0.1-1
- initial package for Fedora