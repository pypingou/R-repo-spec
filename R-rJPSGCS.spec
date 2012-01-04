%global packname  rJPSGCS
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.2.5
Release:          1%{?dist}
Summary:          R-interface to gene drop Java Programs for Statistical Genetics and Computational Statistics (JPSGCS)

Group:            Applications/Engineering 
License:          GPL-3
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.2-5.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-rJava R-chopsticks R-methods 


BuildRequires:    R-devel tex(latex) R-rJava R-chopsticks R-methods



%description
R-interface to gene drop programs from Alun Thomas' Java Programs for
Statistical Genetics and Computational Statistics (JPSGCS)

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
%doc %{rlibdir}/rJPSGCS/DESCRIPTION
%doc %{rlibdir}/rJPSGCS/html
%doc %{rlibdir}/rJPSGCS/NEWS
%{rlibdir}/rJPSGCS/libs
%{rlibdir}/rJPSGCS/Meta
%{rlibdir}/rJPSGCS/java
%{rlibdir}/rJPSGCS/help
%{rlibdir}/rJPSGCS/data
%{rlibdir}/rJPSGCS/NAMESPACE
%{rlibdir}/rJPSGCS/INDEX
%{rlibdir}/rJPSGCS/R

%changelog
* Thu Dec 08 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.2.5-1
- initial package for Fedora