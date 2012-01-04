%global packname  RImageJ
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.3.144
Release:          1%{?dist}
Summary:          R bindings for ImageJ

Group:            Applications/Engineering 
License:          GPL (>= 3.0)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.3-144.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-rJava R-grDevices 

BuildRequires:    R-devel tex(latex) R-rJava R-grDevices 

%description
Bindings between R and the ImageJ java based image processing and Analysis

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
%doc %{rlibdir}/RImageJ/html
%doc %{rlibdir}/RImageJ/DESCRIPTION
%{rlibdir}/RImageJ/R
%{rlibdir}/RImageJ/NAMESPACE
%{rlibdir}/RImageJ/INDEX
%{rlibdir}/RImageJ/help
%{rlibdir}/RImageJ/images
%{rlibdir}/RImageJ/java
%{rlibdir}/RImageJ/Meta

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.3.144-1
- initial package for Fedora