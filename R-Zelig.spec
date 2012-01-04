%global packname  Zelig
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          3.5.3
Release:          1%{?dist}
Summary:          Everyone's Statistical Software

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-MASS R-boot R-stats 

BuildRequires:    R-devel tex(latex) R-MASS R-boot R-stats 

%description
Zelig is an easy-to-use program that can estimate, and help interpret the
results of, an enormous range of statistical models. It literally is
``everyone's statistical software'' because Zelig's simple unified
framework incorporates everyone else's (R) code. We also hope it will
become ``everyone's statistical software'' for applications and teaching,
and so have designed Zelig so that anyone can easily use it or add their
programs to it.  Zelig also comes with infrastructure that facilitates the
use of any existing method, such as by allowing multiply imputed data for
any model, and mimicking the program Clarify (for Stata) that takes the
raw output of existing statistical procedures and translates them into
quantities of direct interest.

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
%doc %{rlibdir}/Zelig/html
%doc %{rlibdir}/Zelig/DESCRIPTION
%doc %{rlibdir}/Zelig/doc
%{rlibdir}/Zelig/demo
%{rlibdir}/Zelig/NAMESPACE
%{rlibdir}/Zelig/zideal
%{rlibdir}/Zelig/LICENSE
%{rlibdir}/Zelig/data
RPM build errors:
%{rlibdir}/Zelig/R
%{rlibdir}/Zelig/Meta
%{rlibdir}/Zelig/help
%{rlibdir}/Zelig/INDEX

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 3.5.3-1
- initial package for Fedora