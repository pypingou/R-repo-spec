%global packname  ChemoSpec
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.48.4
Release:          1%{?dist}
Summary:          Exploratory Chemometrics for Spectroscopy

Group:            Applications/Engineering 
License:          GPL-3
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.48-4.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
A collection of functions for plotting spectra (NMR, IR etc) and carrying
out various forms of top-down exploratory data analysis, such as HCA, PCA
and model-based clustering.  The design allows comparison of data from
samples which fall into groups such as treatment vs. control.  Robust
methods appropriate for this type of high-dimensional data are available. 
ChemoSpec is designed to be very user friendly and suitable for people
with limited background in R.

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
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.48.4-1
- initial package for Fedora