%global packname  sdcMicro
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          2.6.7
Release:          1%{?dist}
Summary:          Statistical Disclosure Control methods for the generation of public- and scientific-use files.

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-robustbase R-tcltk R-car R-cluster R-MASS R-e1071 

BuildRequires:    R-devel tex(latex) R-robustbase R-tcltk R-car R-cluster R-MASS R-e1071 

%description
Data from statistical agencies and other institutions are mostly
confidential. This package can be used for the generation of anonymized
(micro)data, i.e. for the generation of public- and scientific-use files.
The package includes also a graphical user interface.

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
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2.6.7-1
- initial package for Fedora