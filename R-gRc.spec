%global packname  gRc
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.3.0
Release:          1%{?dist}
Summary:          Inference in Graphical Gaussian Models with Edge and Vertex Symmetries

Group:            Applications/Engineering 
License:          GPL
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-gRbase R-graph 

BuildRequires:    R-devel tex(latex) R-gRbase R-graph 

%description
Estimation, model selection and other aspects of statistical inference in
Graphical Gaussian models with edge and vertex symmetries (Graphical
Gaussian models with colours)

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
* Thu Dec 01 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.3.0-1
- initial package for Fedora