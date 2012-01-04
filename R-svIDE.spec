%global packname  svIDE
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.9.50
Release:          1%{?dist}
Summary:          SciViews GUI API - IDE and code editor functions

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.9-50.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core


Requires:         R-utils R-tcltk R-svMisc R-XML 

BuildRequires:    R-devel tex(latex) 
BuildRequires:    R-utils R-tcltk R-svMisc R-XML 


%description
Function for the GUI API to interact with external IDE/code editors

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
%doc %{rlibdir}/svIDE/DESCRIPTION
%doc %{rlibdir}/svIDE/CITATION
%doc %{rlibdir}/svIDE/html
%doc %{rlibdir}/svIDE/NEWS
%{rlibdir}/svIDE/LICENSE
%{rlibdir}/svIDE/R
%{rlibdir}/svIDE/Meta
%{rlibdir}/svIDE/help
%{rlibdir}/svIDE/NAMESPACE
%{rlibdir}/svIDE/INDEX

%changelog
* Thu Dec 08 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.9.50-1
- initial package for Fedora