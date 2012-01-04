%global packname  EBImage
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          3.10.0
Release:          1%{?dist}
Summary:          Image processing toolbox for R

Group:            Applications/Engineering 
License:          Artistic-2.0
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-methods R-graphics R-stats R-utils R-abind 


BuildRequires:    R-devel tex(latex) R-methods R-graphics R-stats R-utils R-abind



%description
EBImage is an R package which provides general purpose functionality for
the reading, writing, processing and analysis of images. Furthermore, in
the context of microscopy based cellular assays, EBImage offers tools to
transform the images, segment cells and extract quantitative cellular

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
* Thu Dec 08 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 3.10.0-1
- initial package for Fedora