%global packname  DIME
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.0
Release:          1%{?dist}
Summary:          DIME (Differential Identification using Mixture Ensemble)

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
A robust differential identification method that considers an ensemble of
finite mixture models combined with a local false discovery rate (fdr) to
analyze ChIP-seq (high-throughput genomic)data comparing two samples
allowing for flexible modeling of data.

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
%doc %{rlibdir}/DIME/html
%doc %{rlibdir}/DIME/DESCRIPTION
%{rlibdir}/DIME/Meta
%{rlibdir}/DIME/help
%{rlibdir}/DIME/INDEX
%{rlibdir}/DIME/R
%{rlibdir}/DIME/libs
%{rlibdir}/DIME/NAMESPACE

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0-1
- initial package for Fedora