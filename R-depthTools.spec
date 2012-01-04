%global packname  depthTools
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.1.0
Release:          1%{?dist}
Summary:          Depth Tools Package

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.1-0.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
depthTools is a package that implements different statistical tools for
the description and analysis of gene expression data based on the concept
of data depth, namely, the scale curves for visualizing the dispersion of
one or various groups of samples (e.g. types of tumors), a rank test to
decide whether two groups of samples come from a single distribution and
two methods of supervised classification techniques, the DS and TAD
methods. All these techniques are based on the Modified Band Depth, which
is a recent notion of depth with a low computational cost, what renders it
very appropriate for high dimensional data such as gene expression data.

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
%doc %{rlibdir}/depthTools/DESCRIPTION
%doc %{rlibdir}/depthTools/html
%{rlibdir}/depthTools/data
%{rlibdir}/depthTools/NAMESPACE
%{rlibdir}/depthTools/R
%{rlibdir}/depthTools/INDEX
%{rlibdir}/depthTools/help
%{rlibdir}/depthTools/Meta

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.1.0-1
- initial package for Fedora