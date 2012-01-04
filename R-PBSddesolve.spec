%global packname  PBSddesolve
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.08.11
Release:          1%{?dist}
Summary:          Solver for Delay Differential Equations

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
This package solves systems of delay differential equations. by
interfacing numerical routines written by Simon N. Wood <s.wood _at_
bath.ac.uk>, with contributions by Benjamin J. Cairns
<ben.cairns@bristol.ac.uk>. These numerical routines first appeared in
Simon Wood's solv95 program. This package includes a vignette and a
complete user's guide. 'PBSddesolve' originally appeared on CRAN under the
name 'ddesolve'. That version is no longer supported. The current name
emphasizes a close association with other PBS packages, particularly

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
%doc %{rlibdir}/PBSddesolve/html
%doc %{rlibdir}/PBSddesolve/doc
%doc %{rlibdir}/PBSddesolve/DESCRIPTION
%{rlibdir}/PBSddesolve/libs
%{rlibdir}/PBSddesolve/demo
%{rlibdir}/PBSddesolve/tests
%{rlibdir}/PBSddesolve/Meta
%{rlibdir}/PBSddesolve/NAMESPACE
%{rlibdir}/PBSddesolve/R
%{rlibdir}/PBSddesolve/demo_files
%{rlibdir}/PBSddesolve/help
%{rlibdir}/PBSddesolve/INDEX

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.08.11-1
- initial package for Fedora