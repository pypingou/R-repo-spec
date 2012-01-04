%global packname  speedRlibs
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.1.30
Release:          1%{?dist}
Summary:          Package containing the required libraries (jars) for speedR

Group:            Applications/Engineering 
License:          LGPL (>= 2.1)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.1-30.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
speedRlibs is a container for the required libraries (jars) by speedR. 
These libraries are packaged separately, because it is approximately 17 MB
and will not be so often updated like speedR.  Thus it reduces the
download time after the first installation.

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
%doc %{rlibdir}/speedRlibs/DESCRIPTION
%doc %{rlibdir}/speedRlibs/html
%{rlibdir}/speedRlibs/Meta
%{rlibdir}/speedRlibs/NOTICE
%{rlibdir}/speedRlibs/java
%{rlibdir}/speedRlibs/R
%{rlibdir}/speedRlibs/NAMESPACE
%{rlibdir}/speedRlibs/help
%{rlibdir}/speedRlibs/INDEX

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.1.30-1
- initial package for Fedora