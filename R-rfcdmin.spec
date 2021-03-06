%global packname  rfcdmin
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.6.11
Release:          1%{?dist}
Summary:          Minimal Data Library for RFlowCyt examples

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://bioconductor.org/packages/release/data/experiment/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/data/experiment/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
Provides basic data sets for examples and should be loaded before the
package 'rflowcyt' and 'rfcprim'.

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
%doc %{rlibdir}/rfcdmin/DESCRIPTION
%doc %{rlibdir}/rfcdmin/html
%{rlibdir}/rfcdmin/fcs
%{rlibdir}/rfcdmin/bccrc
%{rlibdir}/rfcdmin/Meta
%{rlibdir}/rfcdmin/INDEX
%{rlibdir}/rfcdmin/NAMESPACE
%{rlibdir}/rfcdmin/help
%{rlibdir}/rfcdmin/data

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.6.11-1
- initial package for Fedora