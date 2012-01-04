%global packname  RNiftyReg
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.5.0
Release:          1%{?dist}
Summary:          Medical image registration using the NiftyReg library

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)


Requires:         R-reportr 

BuildRequires:    R-devel tex(latex) 
BuildRequires:    R-reportr 


%description
This package provides an R interface to the NiftyReg image registration
tools <http://sourceforge.net/projects/niftyreg/>.

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
%doc %{rlibdir}/RNiftyReg/DESCRIPTION
%doc %{rlibdir}/RNiftyReg/LICENCE
%doc %{rlibdir}/RNiftyReg/html
%doc %{rlibdir}/RNiftyReg/NEWS
%{rlibdir}/RNiftyReg/R
%{rlibdir}/RNiftyReg/libs
%{rlibdir}/RNiftyReg/NAMESPACE
%{rlibdir}/RNiftyReg/help
%{rlibdir}/RNiftyReg/Meta
%{rlibdir}/RNiftyReg/INDEX

%changelog
* Thu Dec 08 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.5.0-1
- initial package for Fedora