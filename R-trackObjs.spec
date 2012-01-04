%global packname  trackObjs
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.8.6
Release:          1%{?dist}
Summary:          Track Objects

Group:            Applications/Engineering 
License:          GPL
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.8-6.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
Stores objects in files on disk so that files are automatically rewritten
when objects are changed, and so that objects are accessible but do not
occupy memory until they are accessed. Also tracks times when objects are
created and modified, and caches some basic characteristics of objects to
allow for fast summaries of objects.

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
%doc %{rlibdir}/trackObjs/NEWS
%doc %{rlibdir}/trackObjs/DESCRIPTION
%doc %{rlibdir}/trackObjs/html
%{rlibdir}/trackObjs/Meta
%{rlibdir}/trackObjs/performanceTrials
%{rlibdir}/trackObjs/R
%{rlibdir}/trackObjs/INDEX
%{rlibdir}/trackObjs/NAMESPACE
%{rlibdir}/trackObjs/help

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.8.6-1
- initial package for Fedora