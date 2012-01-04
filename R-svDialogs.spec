%global packname  svDialogs
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.9.43
Release:          1%{?dist}
Summary:          SciViews GUI API - Dialog boxes

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.9-43.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-tcltk 
Requires:         R-svMisc 

BuildRequires:    R-devel tex(latex) R-tcltk
BuildRequires:    R-svMisc 


%description
Rapidly construct dialog boxes for your GUI, including an automatic
function assistant

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
%doc %{rlibdir}/svDialogs/html
%doc %{rlibdir}/svDialogs/NEWS
%doc %{rlibdir}/svDialogs/DESCRIPTION
%doc %{rlibdir}/svDialogs/CITATION
%{rlibdir}/svDialogs/help
%{rlibdir}/svDialogs/LICENSE
%{rlibdir}/svDialogs/INDEX
%{rlibdir}/svDialogs/Meta
%{rlibdir}/svDialogs/NAMESPACE
%{rlibdir}/svDialogs/R

%changelog
* Thu Dec 08 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.9.43-1
- initial package for Fedora