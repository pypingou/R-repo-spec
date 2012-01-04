%global packname  TargetSearch
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.10.1
Release:          1%{?dist}
Summary:          A package for the analysis of GC-MS metabolite profiling data.

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-xcms R-methods 
Requires:         R-graphics R-grDevices R-methods R-stats R-tcltk R-utils 

BuildRequires:    R-devel tex(latex) R-xcms R-methods
BuildRequires:    R-graphics R-grDevices R-methods R-stats R-tcltk R-utils 


%description
This packages provides a targeted pre-processing method for GC-MS data.

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
* Thu Dec 08 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.10.1-1
- initial package for Fedora