%global packname  nnDiag
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.0.5
Release:          1%{?dist}
Summary:          k-Nearest Neighbor Diagnostic Tools

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.0-5.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-sp R-rgdal R-spBayes R-gplots R-vcd R-MASS R-MBA R-fields R-yaImpute R-geoR 


BuildRequires:    R-devel tex(latex) R-sp R-rgdal R-spBayes R-gplots R-vcd R-MASS R-MBA R-fields R-yaImpute R-geoR



%description
A suite of graphical diagnostic tools to evaluate kNN classifications.

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
* Sat Dec 10 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.0.5-1
- initial package for Fedora