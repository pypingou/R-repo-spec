%global packname  digest
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.5.1
Release:          1%{?dist}
Summary:          Create cryptographic hash digests of R objects

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
The digest package provides a function 'digest()' for the creation of hash
digests of arbitrary R objects (using the md5, sha-1, sha-256 and crc32
algorithms) permitting easy comparison of R language objects, as well as a
function 'hmac()' to create hash-based message authentication code. . The
md5 algorithm by Ron Rivest is specified in RFC 1321, the SHA-1 and
SHA-256 algorithms are specified in FIPS-180-1 and FIPS-180-2, and the
crc32 algorithm is described in
ftp://ftp.rocksoft.com/cliens/rocksoft/papers/crc_v3.txt. For md5, sha-1
and sha-256, this packages uses small standalone implementations that were
provided by Christophe Devine. For crc32, code from the zlib library is
used. . Please note that this package is not meant to be deployed for
cryptographic purposes for which more comprehensive (and widely tested)
libraries such as OpenSSL should be used.

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
%doc %{rlibdir}/digest/DESCRIPTION
%doc %{rlibdir}/digest/html
%{rlibdir}/digest/help
%{rlibdir}/digest/libs
%{rlibdir}/digest/Meta
%{rlibdir}/digest/R
%{rlibdir}/digest/NAMESPACE
%{rlibdir}/digest/INDEX

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.5.1-1
- initial package for Fedora