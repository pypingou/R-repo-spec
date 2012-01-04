%global packname  fdrame
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.26.0
Release:          1%{?dist}
Summary:          FDR adjustments of Microarray Experiments (FDR-AME)

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
This package contains two main functions. The first is fdr.ma which takes
normalized expression data array, experimental design and computes
adjusted p-values It returns the fdr adjusted p-values and plots,
according to the methods described in (Reiner, Yekutieli and Benjamini
2002). The second, is fdr.gui() which creates a simple graphic user
interface to access fdr.ma

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
%doc %{rlibdir}/fdrame/DESCRIPTION
%doc %{rlibdir}/fdrame/doc
%doc %{rlibdir}/fdrame/html
%{rlibdir}/fdrame/libs
%{rlibdir}/fdrame/data
%{rlibdir}/fdrame/Meta
%{rlibdir}/fdrame/help
%{rlibdir}/fdrame/R
%{rlibdir}/fdrame/INDEX
%{rlibdir}/fdrame/NAMESPACE

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.26.0-1
- initial package for Fedora