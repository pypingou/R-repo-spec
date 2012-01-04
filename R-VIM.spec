%global packname  VIM
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          2.0.4
Release:          1%{?dist}
Summary:          Visualization and Imputation of Missing Values

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-e1071 R-car R-colorspace R-nnet R-robustbase R-tcltk R-tkrplot R-sp R-vcd R-Rcpp 
Requires:         R-car R-colorspace R-grDevices R-robustbase R-stats R-tcltk R-sp R-utils R-vcd 

BuildRequires:    R-devel tex(latex) R-e1071 R-car R-colorspace R-nnet R-robustbase R-tcltk R-tkrplot R-sp R-vcd R-Rcpp
BuildRequires:    R-car R-colorspace R-grDevices R-robustbase R-stats R-tcltk R-sp R-utils R-vcd 


%description
This package introduces new tools for the visualization of missing values
in R, which can be used for exploring the data and the structure of the
missing values. Depending on this structure, they may help to identify the
mechanism generating the missings. A graphical user interface allows an
easy handling of the implemented plot methods.

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
* Fri Dec 09 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2.0.4-1
- initial package for Fedora