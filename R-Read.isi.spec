%global packname  Read.isi
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.5.1
Release:          1%{?dist}
Summary:          Automated access to old World Fertility Survey data saved in fixed-width format based on ISI-formatted codebooks.

Group:            Applications/Engineering 
License:          GPL-3
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
Old statistical data was often stored in formats that are difficult to
gain access to by modern statistical software. An example of this are the
data-files of the `World Fertility Survey', which are stored in
fixed-width format and accompanied by codebooks in a format developed by
the International Statistical Institute. The read.isi package allows to
gain access to these statistical data automatically, or to convert to
codebook to SPSS-syntax.

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
%doc %{rlibdir}/Read.isi/DESCRIPTION
%doc %{rlibdir}/Read.isi/CITATION
%doc %{rlibdir}/Read.isi/html
%{rlibdir}/Read.isi/Meta
%{rlibdir}/Read.isi/INDEX
%{rlibdir}/Read.isi/R
%{rlibdir}/Read.isi/NAMESPACE
%{rlibdir}/Read.isi/help

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.5.1-1
- initial package for Fedora