%global packname  JGR
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.7.9
Release:          1%{?dist}
Summary:          JGR - Java Gui for R

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.7-9.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-rJava R-JavaGD R-iplots 


BuildRequires:    R-devel tex(latex) R-rJava R-JavaGD R-iplots



%description
Java GUI for R - cross-platform, universal and unified Graphical User
Interface for R. For full functionality on Windows and Mac OS X JGR
requires a start application which depends on your OS. This can be
downloaded from JGR's website: http://rforge.net/JGR/

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
* Fri Dec 09 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.7.9-1
- initial package for Fedora