%global packname  rcdklibs
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.4.5
Release:          1%{?dist}
Summary:          rcdklib - CDK libraries packaged for R

Group:            Applications/Engineering 
License:          LGPL
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-rJava 

BuildRequires:    R-devel tex(latex) R-rJava 

%description
This package provides the CDK libraries for use in the R environment.
Given the size of the library itself, this package is not expected to
change very frequently. To make use of the CDK within R, it is suggested
that you use the rcdk package. Note that it is possible to directly
interact with the CDK using rJava. However rcdk exposes functionality in a
more idiomatic way

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
%doc %{rlibdir}/rcdklibs/html
%doc %{rlibdir}/rcdklibs/DESCRIPTION
%doc %{rlibdir}/rcdklibs/NEWS
%{rlibdir}/rcdklibs/help
%{rlibdir}/rcdklibs/INDEX
%{rlibdir}/rcdklibs/cont
%{rlibdir}/rcdklibs/R
%{rlibdir}/rcdklibs/NAMESPACE
%{rlibdir}/rcdklibs/Meta

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.4.5-1
- initial package for Fedora