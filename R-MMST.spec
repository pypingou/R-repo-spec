%global packname  MMST
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.6.1.1
Release:          1%{?dist}
Summary:          DATASETS FROM MMST

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.6-1.1.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
The datasets from Modern Multivariate Statistical Techniques by Alan
Julian Izenman are contained in this package.  The documentation
descriptions show the page numbers of references to the data set within
the text.  See the text for detailed descriptions of the datasets.  Also
included in this package is a function for exporting these datasets en

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
%doc %{rlibdir}/MMST/html
%doc %{rlibdir}/MMST/DESCRIPTION
%{rlibdir}/MMST/R
%{rlibdir}/MMST/NAMESPACE
%{rlibdir}/MMST/Meta
%{rlibdir}/MMST/data
%{rlibdir}/MMST/help
%{rlibdir}/MMST/INDEX

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.6.1.1-1
- initial package for Fedora