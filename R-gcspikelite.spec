%global packname  gcspikelite
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.0.6
Release:          1%{?dist}
Summary:          Spike-in data for GC/MS data and methods within flagme

Group:            Applications/Engineering 
License:          LGPL
URL:              http://bioconductor.org/packages/release/data/experiment/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/data/experiment/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
Spike-in data for GC/MS data and methods within flagme

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
%doc %{rlibdir}/gcspikelite/html
%doc %{rlibdir}/gcspikelite/DESCRIPTION
%{rlibdir}/gcspikelite/INDEX
%{rlibdir}/gcspikelite/data
%{rlibdir}/gcspikelite/R
%{rlibdir}/gcspikelite/NAMESPACE
%{rlibdir}/gcspikelite/Meta
%{rlibdir}/gcspikelite/help

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.6-1
- initial package for Fedora