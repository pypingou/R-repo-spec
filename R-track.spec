%global packname  track
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.0.1
Release:          1%{?dist}
Summary:          Track Objects

Group:            Applications/Engineering 
License:          GPL
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.0-1.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
Automatically stores objects in files on disk so that files are rewritten
when objects are changed, and so that objects are accessible but do not
occupy memory until they are accessed. Keeps track of times when objects
are created and modified, and caches some basic characteristics of objects
to allow for fast summaries of objects.  Also provides a command history
mechanism that saves the last command to a history file after each command

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
%doc %{rlibdir}/track/html
%doc %{rlibdir}/track/DESCRIPTION
%doc %{rlibdir}/track/NEWS
%doc %{rlibdir}/track/doc
%{rlibdir}/track/NAMESPACE
%{rlibdir}/track/R
%{rlibdir}/track/Meta
%{rlibdir}/track/performanceTrials
%{rlibdir}/track/help
%{rlibdir}/track/INDEX

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.1-1
- initial package for Fedora