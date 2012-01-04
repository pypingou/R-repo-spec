%global packname  ROI.plugin.glpk
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.0.1
Release:          1%{?dist}
Summary:          ROI-plugin GLPK

Group:            Applications/Engineering 
License:          GPL-3
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.0-1.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core


Requires:         R-methods R-ROI R-Rglpk 

BuildRequires:    R-devel tex(latex) 
BuildRequires:    R-methods R-ROI R-Rglpk 


%description
This package enhances the R Optimization Infrastructure (ROI) package with
the GLPK solver for solving mixed integer linear programming (MILP)
problems as well as all variants/combinations of LP, IP.

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
%doc %{rlibdir}/ROI.plugin.glpk/html
%doc %{rlibdir}/ROI.plugin.glpk/DESCRIPTION
%{rlibdir}/ROI.plugin.glpk/R
%{rlibdir}/ROI.plugin.glpk/NAMESPACE
%{rlibdir}/ROI.plugin.glpk/help
%{rlibdir}/ROI.plugin.glpk/Meta

%changelog
* Fri Dec 09 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.0.1-1
- initial package for Fedora