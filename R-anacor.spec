%global packname  anacor
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.0.1
Release:          1%{?dist}
Summary:          Simple and Canonical Correspondence Analysis.

Group:            Applications/Engineering 
License:          GPL
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.0-1.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-rgl R-scatterplot3d R-fda R-colorspace R-car 
Requires:         R-graphics R-stats 

BuildRequires:    R-devel tex(latex) R-rgl R-scatterplot3d R-fda R-colorspace R-car
BuildRequires:    R-graphics R-stats 


%description
This package performs simple and canonical CA (covariates on rows/columns)
on a two-way frequency table (with missings) by means of SVD. Different
scaling methods (standard, centroid, Benzecri, Goodman) as well as various
plots including confidence ellipsoids are provided.

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
* Fri Dec 09 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.1-1
- initial package for Fedora