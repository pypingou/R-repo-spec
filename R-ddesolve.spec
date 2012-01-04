%global packname  ddesolve
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.04
Release:          1%{?dist}
Summary:          Solver for Delay Differential Equations

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
***** This package is DEPRECATED. ***** Download the package 'PBSddesolve'
to solve systems of delay differential equations using numerical routines
written by Simon N. Wood <s.wood _at_ bath.ac.uk>, with contributions by
Benjamin J. Cairns <ben.cairns@bristol.ac.uk>. These numerical routines
first appeared in Simon Wood's solv95 program.

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
%doc %{rlibdir}/ddesolve/html
%doc %{rlibdir}/ddesolve/doc
%doc %{rlibdir}/ddesolve/DESCRIPTION
%{rlibdir}/ddesolve/R
%{rlibdir}/ddesolve/NAMESPACE
%{rlibdir}/ddesolve/Meta
%{rlibdir}/ddesolve/help
%{rlibdir}/ddesolve/INDEX
%{rlibdir}/ddesolve/License.txt

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.04-1
- initial package for Fedora