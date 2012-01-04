%global packname  speedR
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.1.32
Release:          1%{?dist}
Summary:          A GUI based importing and filtering tool

Group:            Applications/Engineering 
License:          LGPL (>= 2.1)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.1-32.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-rJava R-speedRlibs R-speedRlibTF 

BuildRequires:    R-devel tex(latex) R-rJava R-speedRlibs R-speedRlibTF 

%description
speedR is a gui based utility to import and to filter matrix alike data
objects easily.

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
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.1.32-1
- initial package for Fedora