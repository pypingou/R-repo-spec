%global packname  svSocket
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.9.51
Release:          1%{?dist}
Summary:          SciViews GUI API - R Socket Server

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.9-51.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core


Requires:         R-tcltk R-svMisc 

BuildRequires:    R-devel tex(latex) 
BuildRequires:    R-tcltk R-svMisc 


%description
Implements a simple socket server allowing to connect GUI clients to R

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
%doc %{rlibdir}/svSocket/NEWS
%doc %{rlibdir}/svSocket/html
%doc %{rlibdir}/svSocket/CITATION
%doc %{rlibdir}/svSocket/DESCRIPTION
%{rlibdir}/svSocket/NAMESPACE
%{rlibdir}/svSocket/LICENSE
%{rlibdir}/svSocket/Meta
%{rlibdir}/svSocket/etc
%{rlibdir}/svSocket/INDEX
%{rlibdir}/svSocket/R
%{rlibdir}/svSocket/help

%changelog
* Thu Dec 08 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.9.51-1
- initial package for Fedora