%global packname  ant
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.0.10
Release:          1%{?dist}
Summary:          Version of ant specific to R

Group:            Applications/Engineering 
License:          Apache License (== 2.0)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.0-10.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-rJava 

BuildRequires:    R-devel tex(latex) R-rJava 

%description
Version of the ant apache build tool, with a few R specific tasks to ease
use of ant within an R package

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
%doc %{rlibdir}/ant/html
%doc %{rlibdir}/ant/DESCRIPTION
%{rlibdir}/ant/R
%{rlibdir}/ant/apache-ant
%{rlibdir}/ant/Meta
%{rlibdir}/ant/INDEX
%{rlibdir}/ant/examples
%{rlibdir}/ant/NAMESPACE
%{rlibdir}/ant/java_src
%{rlibdir}/ant/cleanup
%{rlibdir}/ant/help
%{rlibdir}/ant/exec

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.0.10-1
- initial package for Fedora