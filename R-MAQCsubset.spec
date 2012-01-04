%global packname  MAQCsubset
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.0.24
Release:          1%{?dist}
Summary:          Experimental Data Package: MAQCsubset

Group:            Applications/Engineering 
License:          Artistic-2.0
URL:              http://bioconductor.org/packages/release/data/experiment/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/data/experiment/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-affy R-Biobase R-lumi R-methods 

BuildRequires:    R-devel tex(latex) R-affy R-Biobase R-lumi R-methods 

%description
Data Package automatically created on Sun Nov 19 15:59:29 2006.

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
* Fri Dec 02 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.24-1
- initial package for Fedora