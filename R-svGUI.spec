%global packname  svGUI
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.9.50
Release:          1%{?dist}
Summary:          SciViews GUI API - Functions to manage GUI client

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.9-50.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-svMisc 

BuildRequires:    R-devel tex(latex) R-svMisc 

%description
Functions to manage the GUI client, like Komodo with the SciViews-K

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
%doc %{rlibdir}/svGUI/DESCRIPTION
%doc %{rlibdir}/svGUI/CITATION
%doc %{rlibdir}/svGUI/NEWS
%doc %{rlibdir}/svGUI/html
%{rlibdir}/svGUI/LICENSE
%{rlibdir}/svGUI/R
%{rlibdir}/svGUI/NAMESPACE
%{rlibdir}/svGUI/INDEX
%{rlibdir}/svGUI/help
%{rlibdir}/svGUI/Meta

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.9.50-1
- initial package for Fedora