%global packname  seqRFLP
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.0.1
Release:          1%{?dist}
Summary:          Simulation and visualization of restriction enzyme cutting pattern from DNA sequences.

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
This package includes functions for handling DNA sequences, especially
simulated RFLP and TRFLP pattern based on selected restriction enzyme and
DNA sequences.

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
%doc %{rlibdir}/seqRFLP/html
%doc %{rlibdir}/seqRFLP/DESCRIPTION
%{rlibdir}/seqRFLP/NAMESPACE
%{rlibdir}/seqRFLP/extdata
%{rlibdir}/seqRFLP/INDEX
%{rlibdir}/seqRFLP/help
%{rlibdir}/seqRFLP/data
%{rlibdir}/seqRFLP/Meta
%{rlibdir}/seqRFLP/R

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.1-1
- initial package for Fedora