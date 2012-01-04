%global packname  gnumeric
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.7.1
Release:          1%{?dist}
Summary:          Read data from files readable by gnumeric

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.7-1.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-XML 

BuildRequires:    R-devel tex(latex) R-XML 

%description
Read data files readable by gnumeric into R. Can read whole sheet or a
range, from several file formats, including the native format of gnumeric.
Reading is done by using ssconvert (a file converter utility included in
the gnumeric distribution http://projects.gnome.org/gnumeric/) to convert
the requested part to CSV. From gnumeric files (but not other formats) can
list sheet names and sheet sizes or read all sheets.

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
%doc %{rlibdir}/gnumeric/DESCRIPTION
%doc %{rlibdir}/gnumeric/html
%{rlibdir}/gnumeric/Meta
%{rlibdir}/gnumeric/INDEX
%{rlibdir}/gnumeric/R
%{rlibdir}/gnumeric/help

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.7.1-1
- initial package for Fedora