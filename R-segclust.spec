%global packname  segclust
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.76
Release:          1%{?dist}
Summary:          SegClust : a package for Segmentation and Segmentation/Clustering.

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
SegClust corresponds to the implementation of the statistical model
described in : Picard et al., A segmentation/clustering model for the
analysis of array CGH data. Biometrics, 63(3) 2007. Segmentation functions
are also available (from Picard et al. A statistical approach for array
CGH data analysis. BMC Bioinformatics. 2005 Feb 11;6:27).

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
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.76-1
- initial package for Fedora