%global packname  flowWorkspaceData
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.99.6
Release:          1%{?dist}
Summary:          A data package containing a flowJo xml workspace and associated fcs files for testing the flowWorkspace package.

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://bioconductor.org/packages/release/data/experiment/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/data/experiment/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
The necessary external data to run the flowWorkspace vignette is found in
this package.

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
%doc %{rlibdir}/flowWorkspaceData/DESCRIPTION
%doc %{rlibdir}/flowWorkspaceData/html
%{rlibdir}/flowWorkspaceData/Meta
%{rlibdir}/flowWorkspaceData/INDEX
%{rlibdir}/flowWorkspaceData/NAMESPACE
%{rlibdir}/flowWorkspaceData/extdata
%{rlibdir}/flowWorkspaceData/R
%{rlibdir}/flowWorkspaceData/help

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.99.6-1
- initial package for Fedora