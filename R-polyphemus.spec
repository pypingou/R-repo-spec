%global packname  polyphemus
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.3.4
Release:          1%{?dist}
Summary:          Genome wide analysis of RNA Polymerase II-based ChIP Seq data.

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core


Requires:         R-IRanges R-zoo R-RUnit R-parallel R-R.utils R-limma 

BuildRequires:    R-devel tex(latex) 
BuildRequires:    R-IRanges R-zoo R-RUnit R-parallel R-R.utils R-limma 


%description
Polyphemus is able to combine signal intensity (count) profiles, with
significant peak annotations in order to identify coding regions of
interest for the comparative analysis or two or more samples. The
algorithm (i) identifies significant coding regions, (ii) performs
normalization, (iii) compares several profiles and (iv) provides matrix
output suitable for further clustering analysis.

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
%changelog
* Sat Dec 10 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.3.4-1
- initial package for Fedora