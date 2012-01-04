%global packname  ROI.plugin.quadprog
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.0.1
Release:          1%{?dist}
Summary:          ROI-plugin quadprog

Group:            Applications/Engineering 
License:          GPL-3
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.0-1.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core


Requires:         R-methods R-ROI R-quadprog 

BuildRequires:    R-devel tex(latex) 
BuildRequires:    R-methods R-ROI R-quadprog 


%description
This package enhances the R Optimization Infrastructure (ROI) package with
the quadprog solver for solving quadratic programming (QP) problems.

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
%doc %{rlibdir}/ROI.plugin.quadprog/html
%doc %{rlibdir}/ROI.plugin.quadprog/DESCRIPTION
%{rlibdir}/ROI.plugin.quadprog/help
%{rlibdir}/ROI.plugin.quadprog/R
%{rlibdir}/ROI.plugin.quadprog/NAMESPACE
%{rlibdir}/ROI.plugin.quadprog/Meta

%changelog
* Fri Dec 09 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.0.1-1
- initial package for Fedora